from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json

from .models import CarMake, CarModel, Dealer, Review
from .serializers import CarMakeSerializer, DealerSerializer, ReviewSerializer

# ---------- Mock Sentiment Analysis ----------
def analyze_sentiment(text):
    """Mock: returns positive/neutral/negative based on keywords."""
    positive_words = ['fantastic', 'great', 'excellent', 'amazing', 'love']
    negative_words = ['terrible', 'awful', 'bad', 'hate', 'poor']
    text_lower = text.lower()
    if any(word in text_lower for word in positive_words):
        return 'positive'
    elif any(word in text_lower for word in negative_words):
        return 'negative'
    return 'neutral'

# ---------- Authentication ----------
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'username': user.username})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
    return JsonResponse({'status': 'error'}, status=405)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'logged out'})
    return JsonResponse({'status': 'error'}, status=405)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'message': 'Username exists'}, status=400)
        user = User.objects.create_user(username=username, password=password,
                                        first_name=first_name, last_name=last_name, email=email)
        return JsonResponse({'status': 'success', 'username': user.username})
    return JsonResponse({'status': 'error'}, status=405)

@api_view(['GET'])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({'username': request.user.username})
    return Response({'username': None})

# ---------- Car Makes / Models ----------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_car_makes(request):
    makes = CarMake.objects.all()
    data = []
    for make in makes:
        models = list(CarModel.objects.filter(car_make=make).values_list('name', flat=True))
        data.append({'make': make.name, 'models': models})
    return Response(data)

# ---------- Dealers ----------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_dealers(request):
    dealers = Dealer.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_by_id(request):
    dealer_id = request.GET.get('id')
    if dealer_id:
        try:
            dealer = Dealer.objects.get(pk=dealer_id)
            serializer = DealerSerializer(dealer)
            return Response(serializer.data)
        except Dealer.DoesNotExist:
            return Response({'error': 'Dealer not found'}, status=404)
    return Response({'error': 'Missing id'}, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers_by_state(request):
    state = request.GET.get('state')
    if state:
        dealers = Dealer.objects.filter(state__iexact=state)
        serializer = DealerSerializer(dealers, many=True)
        return Response(serializer.data)
    return Response({'error': 'Missing state'}, status=400)

# ---------- Reviews ----------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_reviews(request):
    dealer_id = request.GET.get('dealer_id')
    if dealer_id:
        reviews = Review.objects.filter(dealer_id=dealer_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    return Response({'error': 'Missing dealer_id'}, status=400)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_review(request):
    data = json.loads(request.body)
    dealer_id = data.get('dealer_id')
    review_text = data.get('review_text')
    purchase = data.get('purchase', False)
    car_make_name = data.get('car_make')
    car_model_name = data.get('car_model')
    try:
        dealer = Dealer.objects.get(pk=dealer_id)
    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=404)
    sentiment = analyze_sentiment(review_text)
    car_make = None
    car_model = None
    if car_make_name:
        car_make, _ = CarMake.objects.get_or_create(name=car_make_name)
    if car_model_name and car_make:
        car_model, _ = CarModel.objects.get_or_create(name=car_model_name, car_make=car_make)
    review = Review.objects.create(
        dealer=dealer,
        user=request.user,
        review_text=review_text,
        sentiment=sentiment,
        purchase=purchase,
        car_make=car_make,
        car_model=car_model
    )
    return Response({'status': 'review created', 'sentiment': sentiment})

# ---------- Sentiment Analysis Endpoint ----------
@api_view(['POST'])
@permission_classes([AllowAny])
def analyze_review_api(request):
    text = request.data.get('review_text', '')
    sentiment = analyze_sentiment(text)
    return Response({'sentiment': sentiment})