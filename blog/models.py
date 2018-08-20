from django.db import models
from django.utils import timezone

# on_delete = models.CASCADE 설정시 A:B가 N:1관계일 때, B의 어떤 레코드가 삭제되면 삭제될 모델 B의 레코드와 관련있는 모델 A의 레코드들도 연차적으로 삭제됨
# ON_DELETE가 설정되어있지 않으면 모델 B의 레코드를 참조하고 있는 다른 모델의 레코드가 있기때문에 삭제할 수 없음
# models.CharField : 글자수가 제한된 텍스트를 정의할 때 사용

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	creaded_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)


# publish메서드, __str__메서드
def publish(self):
	self.published_date = timezone.now()
	self.save()

# __str__을 호출하면 Post모델의 title 텍스트를 얻게 됨
def __str__(self):
	return self.title



#### cmd에서 python manage.py migrations blog를 통해 장고 모델에 변화가 생겼다는 걸 알림
#### cmd에서 python manage.py migrate blog를 통해 실제 DB에 모델 추가를 반영함