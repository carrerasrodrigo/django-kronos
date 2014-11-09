from django.core.management.base import NoArgsCommand
from kronos import tasks, reinstall


class Command(NoArgsCommand):
    help = 'Register tasks with cron'

    def handle_noargs(self, **options):
        reinstall()
        print "Installed %s tasks." % len(tasks)
