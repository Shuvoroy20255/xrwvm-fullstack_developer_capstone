from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.get(user=request.user, course=course)
    questions = course.question_set.all()
    submission = Submission.objects.create(enrollment=enrollment)
    
    for question in questions:
        selected_id = request.POST.get(str(question.id))
        if selected_id:
            selected_choice = Choice.objects.get(pk=selected_id)
            submission.choices.add(selected_choice)
    submission.save()
    
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result',
                                        args=(course_id, submission.id)))

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(pk=submission_id)
    choices = submission.choices.all()
    
    total_score = 0
    for question in course.question_set.all():
        correct = set(question.choice_set.filter(is_correct=True))
        selected = set(choices.filter(question=question))
        if correct == selected:
            total_score += question.grade
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {
        'course': course,
        'submission': submission,
        'total_score': total_score,
    })
