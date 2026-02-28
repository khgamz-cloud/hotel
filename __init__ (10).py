{% extends 'base.html' %}
{% block content %}
<div class="hero-card p-4 p-md-5 mb-4 rounded-4 text-white">
  <h1 class="display-6 fw-bold">Бронирование номеров онлайн</h1>
  <p class="lead mb-0">Выберите номер, проверьте стоимость и оформите бронирование через публичную часть приложения.</p>
</div>
<div class="row g-4">
  {% for room in rooms %}
  <div class="col-md-6 col-lg-4">
    <div class="card h-100 shadow-sm border-0 rounded-4">
      <div class="card-body">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <h2 class="h5 mb-0">Номер {{ room.number }}</h2>
          <span class="badge bg-success">{{ room.category.name }}</span>
        </div>
        <p class="text-muted mb-2">Этаж: {{ room.floor }} · Вместимость: {{ room.capacity }}</p>
        <p class="mb-3">{{ room.category.description }}</p>
        <div class="fw-semibold fs-5 mb-3">{{ '%.0f'|format(room.price) }} ₽ / ночь</div>
        <a class="btn btn-primary" href="{{ url_for('public.room_detail', room_id=room.id) }}">Забронировать</a>
      </div>
    </div>
  </div>
  {% else %}
  <p>Нет доступных номеров.</p>
  {% endfor %}
</div>
{% endblock %}
