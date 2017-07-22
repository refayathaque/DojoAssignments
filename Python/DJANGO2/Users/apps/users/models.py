from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User: {} {} {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.age, self.created_at, self.updated_at)

# >>> User.objects.create(first_name="Refayat", last_name="Haque", email="refayathaque@gmail.com", age=27)
# <User: User object>
# >>> User.objects.create(first_name="Bulus", last_name="Haque", email="bulus@gmail.com", age=13)
# <User: User object>
# >>> User.objects.create(first_name="Ishaba", last_name="Haque", email="ishaba@gmail.com", age=22)
# <User: User object>

# >>> User.objects.all()
# <QuerySet [<User: Refayat Haque refayathaque@gmail.com 27 2017-07-22 17:46:43.373235+00:00 2017-07-22 17:46:43.373351+00:00>, <User: Bulus Haque bulus@gmail.com 13 2017-07-22 17:47:05.073466+00:00 2017-07-22 17:47:05.073551+00:00>, <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 17:47:47.938747+00:00 2017-07-22 17:47:47.938833+00:00>, <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 18:24:17.225850+00:00 2017-07-22 18:24:17.225976+00:00>, <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 18:29:21.602566+00:00 2017-07-22 18:29:21.602686+00:00>, <User: IshabaIshaba Haque ishaba@gmail.com 22 2017-07-22 18:29:48.068261+00:00 2017-07-22 18:29:48.068348+00:00>, <User: I Haque ishaba@gmail.com 22 2017-07-22 18:31:11.864321+00:00 2017-07-22 18:31:11.864412+00:00>, <User: Refayat Haque refayathaque@gmail.com 27 2017-07-22 18:32:14.388208+00:00 2017-07-22 18:32:14.388322+00:00>]>

# User.objects.first()
# <User: Refayat Haque refayathaque@gmail.com 27 2017-07-22 17:46:43.373235+00:00 2017-07-22 17:46:43.373351+00:00>

# >>> User.objects.last()
# <User: Refayat Haque refayathaque@gmail.com 27 2017-07-22 18:32:14.388208+00:00 2017-07-22 18:32:14.388322+00:00>

# >>> User.objects.order_by("-first_name")
# <QuerySet [<User: Refayat Haque refayathaque@gmail.com 27 2017-07-22 17:46:43.373235+00:00 2017-07-22 17:46:43.373351+00:00>, <User: Refayat Haque refayathaque@gmail.com 27 2017-07-22 18:32:14.388208+00:00 2017-07-22 18:32:14.388322+00:00>, <User: IshabaIshaba Haque ishaba@gmail.com 22 2017-07-22 18:29:48.068261+00:00 2017-07-22 18:29:48.068348+00:00>, <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 17:47:47.938747+00:00 2017-07-22 17:47:47.938833+00:00>, <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 18:24:17.225850+00:00 2017-07-22 18:24:17.225976+00:00>, <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 18:29:21.602566+00:00 2017-07-22 18:29:21.602686+00:00>, <User: I Haque ishaba@gmail.com 22 2017-07-22 18:31:11.864321+00:00 2017-07-22 18:31:11.864412+00:00>, <User: Bulus Haque bulus@gmail.com 13 2017-07-22 17:47:05.073466+00:00 2017-07-22 17:47:05.073551+00:00>]>

# >>> User.objects.get(id=3)
# <User: Ishaba Haque ishaba@gmail.com 22 2017-07-22 17:47:47.938747+00:00 2017-07-22 17:47:47.938833+00:00>
# >>> update = User.objects.get(id=3)
# >>> update.last_name = "CHANGEDLASTNAME"
# >>> update.save()
# >>> User.objects.get(id=3)
# <User: Ishaba CHANGEDLASTNAME ishaba@gmail.com 22 2017-07-22 17:47:47.938747+00:00 2017-07-22 19:37:29.899927+00:00>

# User.objects.get(id=4).delete()
# (1, {u'users.User': 1})
