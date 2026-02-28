{% extends 'admin/base.html' %}
{% block admin_content %}
<div class="d-flex justify-content-between align-items-center mb-3"><h1 class="h3 mb-0">Отчётность</h1><a class="btn btn-outline-primary" href="{{ url_for('admin.reports_export') }}">Выгрузить CSV</a></div>
<div class="row g-3 mb-4">
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Бронирований</div><div class="fs-3 fw-bold">{{ stats.total_bookings }}</div></div></div></div>
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Выручка</div><div class="fs-3 fw-bold">{{ stats.total_revenue }} ₽</div></div></div></div>
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Отмены</div><div class="fs-3 fw-bold">{{ stats.cancelled }}</div></div></div></div>
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Топ категория</div><div class="fs-5 fw-bold">{{ stats.top_category }}</div></div></div></div>
</div>
<div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="table-responsive">
<table class="table align-middle">
  <thead><tr><th>ID</th><th>Гость</th><th>Номер</th><th>Заезд</th><th>Выезд</th><th>Сумма</th><th>Статус</th></tr></thead>
  <tbody>
    {% for b in recent %}
      <tr><td>{{ b.id }}</td><td>{{ b.guest_name }}</td><td>{{ b.room.number }}</td><td>{{ b.check_in }}</td><td>{{ b.check_out }}</td><td>{{ b.total_amount }} ₽</td><td>{{ b.status }}</td></tr>
    {% else %}
      <tr><td colspan="7" class="text-center text-muted py-4">Пока нет данных для отчёта.</td></tr>
    {% endfor %}
  </tbody>
</table>
</div></div></div>
{% endblock %}
