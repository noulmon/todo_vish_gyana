from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.models import User

TASK_STATUSES = [
    ('TODO', 'TODO'),
    ('WIP', 'Work In Progress'),
    ('DONE', 'DONE')
]


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(blank=False, null=False, max_length=10, choices=TASK_STATUSES,
                              default=TASK_STATUSES[0][0])
    created_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        db_table = 'TASK'
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        return self.title.__str__()
