from django.urls import path

from habit.apps import HabitConfig
from habit.views import (HabitCreateAPIView, HabitDestroyAPIView, HabitPrivateListAPIView, HabitPrivateRetrieveAPIView,
                         HabitPublicListAPIView, HabitPublicRetrieveAPIView, HabitUpdateAPIView)

app_name = HabitConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("public/", HabitPublicListAPIView.as_view(), name="habit_public_list"),
    path("", HabitPrivateListAPIView.as_view(), name="habit_private_list"),
    path("public/<int:pk>/", HabitPublicRetrieveAPIView.as_view(), name="habit_public_retrieve"),
    path("<int:pk>/", HabitPrivateRetrieveAPIView.as_view(), name="habit_private_retrieve"),
    path("edit/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_edit"),
    path("destroy/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_destroy"),
]
