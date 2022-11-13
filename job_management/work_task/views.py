from django.shortcuts import render

data_active_page = {
    'title': 'Рабочее задание',
}

def work_task(request):
    return render(request, 'work_task/task.html', data_active_page)
