from django.shortcuts import render

data_active_page = {
    'title': 'Рабочее задание',
    'css_active': 'nav-link px-2 fs-4 fw-bold text-warning',
    'css_nonactive': 'nav-link px-2 fs-4 text-white'
}


def work_task(request):
    return render(request, 'work_task/task.html', data_active_page)
