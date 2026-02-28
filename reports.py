{% extends 'base.html' %}
{% block content %}
<div class="row justify-content-center">
  <div class="col-md-5">
    <div class="card shadow-sm border-0">
      <div class="card-body p-4">
        <h1 class="h3 mb-3">Вход в админ-панель</h1>
        <form method="post">
          <div class="mb-3">
            <label class="form-label">Email</label>
            <input class="form-control" name="email" type="email" required>
          </div>
          <div class="mb-3">
            <label class="form-label">Пароль</label>
            <input class="form-control" name="password" type="password" required>
          </div>
          <button class="btn btn-primary w-100">Войти</button>
        </form>
        <div class="small text-muted mt-3">Демо-пользователь создаётся через CLI: <code>flask create-admin --email admin@hotel.local --password admin123</code></div>
      </div>
    </div>
  </div>
</div>
{% endblock %}
