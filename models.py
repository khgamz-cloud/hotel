{% extends 'admin/base.html' %}
{% block admin_content %}
<h1 class="h3 mb-3">База данных и резервные копии</h1>
<div class="row g-3 mb-4">
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Категорий</div><div class="fs-3 fw-bold">{{ integrity.categories }}</div></div></div></div>
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Номеров</div><div class="fs-3 fw-bold">{{ integrity.rooms }}</div></div></div></div>
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Бронирований</div><div class="fs-3 fw-bold">{{ integrity.bookings }}</div></div></div></div>
  <div class="col-md-3"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="text-muted">Дубликатов №</div><div class="fs-3 fw-bold">{{ integrity.duplicates }}</div></div></div></div>
</div>
<div class="card border-0 shadow-sm rounded-4"><div class="card-body">
  <h2 class="h5">Найденные резервные копии</h2>
  <ul class="list-group list-group-flush">
    {% for file in files %}
      <li class="list-group-item d-flex justify-content-between"><span>{{ file.name }}</span><span class="text-muted">{{ (file.stat().st_size / 1024)|round(1) }} KB</span></li>
    {% else %}
      <li class="list-group-item text-muted">Пока нет резервных копий. Создайте их командой <code>flask db-backup</code>.</li>
    {% endfor %}
  </ul>
</div></div>
{% endblock %}
