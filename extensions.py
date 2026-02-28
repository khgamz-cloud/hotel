{% extends 'admin/base.html' %}
{% block admin_content %}
<h1 class="h3 mb-3">Пользователи и роли</h1>
<div class="row g-4">
  <div class="col-lg-7"><div class="card border-0 shadow-sm rounded-4"><div class="card-body"><div class="table-responsive">
    <table class="table align-middle">
      <thead><tr><th>ФИО</th><th>Email</th><th>Роль</th><th>Статус</th><th></th></tr></thead>
      <tbody>
      {% for u in items %}
      <tr><td>{{ u.full_name }}</td><td>{{ u.email }}</td><td>{{ u.role.name }}</td><td>{% if u.is_active_user %}<span class="badge bg-success">Активен</span>{% else %}<span class="badge bg-secondary">Заблокирован</span>{% endif %}</td><td class="text-end"><a class="btn btn-sm btn-outline-primary" href="{{ url_for('admin.users', edit=u.id) }}">Редактировать</a></td></tr>
      {% endfor %}
      </tbody>
    </table>
  </div></div></div></div>
  <div class="col-lg-5"><div class="card border-0 shadow-sm rounded-4"><div class="card-body">
    <h2 class="h5">{{ 'Редактирование' if edit_item else 'Новый пользователь' }}</h2>
    <form method="post" class="row g-3">
      {% if edit_item %}<input type="hidden" name="user_id" value="{{ edit_item.id }}">{% endif %}
      <div class="col-12"><label class="form-label">ФИО</label><input class="form-control" name="full_name" value="{{ edit_item.full_name if edit_item else '' }}" required></div>
      <div class="col-12"><label class="form-label">Email</label><input class="form-control" type="email" name="email" value="{{ edit_item.email if edit_item else '' }}" required></div>
      <div class="col-md-8"><label class="form-label">Роль</label><select class="form-select" name="role_id">{% for role in roles %}<option value="{{ role.id }}" {% if edit_item and edit_item.role_id == role.id %}selected{% endif %}>{{ role.name }}</option>{% endfor %}</select></div>
      <div class="col-md-4"><label class="form-label">Пароль</label><input class="form-control" type="text" name="password" placeholder="Новый пароль"></div>
      <div class="col-12 form-check ms-1"><input class="form-check-input" type="checkbox" name="is_active" {% if edit_item is none or edit_item.is_active_user %}checked{% endif %}><label class="form-check-label">Активен</label></div>
      <div class="col-12"><button class="btn btn-primary">Сохранить</button></div>
    </form>
  </div></div></div>
</div>
{% endblock %}
