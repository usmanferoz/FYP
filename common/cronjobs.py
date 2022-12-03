from user_project.models import Project , ProjectTask , ProjectStatusChoices
from django.utils import timezone
from user_life.models import UserDay

def auto_complete_project_cronjob():
    try:
        projects = Project.objects.filter()
        print(projects)
        for project in projects:
            total_tasks = project.project_tasks.all().count()
            print(total_tasks)
            total_completed_tasks = project.project_tasks.filter(task_status = True).all().count()
            print(total_completed_tasks)
            if total_completed_tasks == total_tasks:
                project.project_status = ProjectStatusChoices.COMPLETED
                project.save()
                print(project.project_status)
            else:
                project.project_status = ProjectStatusChoices.GOING
                project.save()
                print(project.project_status)
    except Exception as e:
        print("EXCEPTION OCCURED :- " , e)



def delete_user_day_setup():
    try:
        today = timezone.now().date()
        user_days = UserDay.objects.filter(day__lt=today)
        if user_days.exists():
            user_days.delete()
            print("user days delete")
        else:
            print("old user days not found")

    except Exception as e:
        print("EXCEPTION OCCURED :- " , e)




