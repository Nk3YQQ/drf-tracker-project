from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from users.permissions import IsOwner, IsOwnerOrReadOnly


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Чтение всех привычек"""

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitPublicListAPIView(HabitListAPIView):
    """Чтение всех публичных привычек"""

    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class HabitPrivateListAPIView(HabitListAPIView):
    """Чтение всех приватных привычек"""

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Чтение одной привычки"""

    serializer_class = HabitSerializer


class HabitPublicRetrieveAPIView(HabitRetrieveAPIView):
    """Чтение одной публичной привычки"""

    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class HabitPrivateRetrieveAPIView(HabitListAPIView):
    """Чтение одной приватной привычки"""

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Обновление привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
