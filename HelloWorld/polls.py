from polls.models import Poll, Choice  #在这里导入我们刚写好的模型
Poll.objects.all() #查看模型的所有对象，结果必然为空，因为我们还没有创建
from django.utils import timezone
p = Poll(question="What's new?", pub_date=timezone.now())
p.save()
p.id
p.question
p.pub_date