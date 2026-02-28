from .extensions import db
from .models import Permission, Role, User, RoomCategory, Room, Service

PERMISSIONS = [
    ("admin.dashboard.view", "Просмотр панели"),
    ("admin.categories.view", "Просмотр категорий"),
    ("admin.categories.edit", "Редактирование категорий"),
    ("admin.rooms.view", "Просмотр номеров"),
    ("admin.services.view", "Просмотр услуг"),
    ("admin.services.edit", "Редактирование услуг"),
    ("admin.users.view", "Просмотр пользователей"),
    ("admin.users.edit", "Редактирование пользователей"),
    ("admin.reports.view", "Просмотр отчётов"),
    ("admin.db.restore", "Восстановление БД"),
]

ROLE_MAP = {
    "Администратор": [p[0] for p in PERMISSIONS],
    "Менеджер": [
        "admin.dashboard.view", "admin.categories.view", "admin.rooms.view",
        "admin.services.view", "admin.reports.view"
    ],
    "Аудитор": ["admin.dashboard.view", "admin.reports.view"],
}


def seed_all():
    if not Permission.query.first():
        for code, title in PERMISSIONS:
            db.session.add(Permission(code=code, title=title))
        db.session.commit()

    for role_name, perm_codes in ROLE_MAP.items():
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            role = Role(name=role_name, description=f"Роль {role_name}")
            db.session.add(role)
            db.session.flush()
        role.permissions = Permission.query.filter(Permission.code.in_(perm_codes)).all()
    db.session.commit()

    if not RoomCategory.query.first():
        cats = [
            RoomCategory(name="Стандарт", capacity=2, base_price=4500, description="Базовый номер", rules="Без животных"),
            RoomCategory(name="Комфорт", capacity=3, base_price=6800, description="Улучшенная категория", rules="Дети допускаются"),
            RoomCategory(name="Люкс", capacity=4, base_price=11900, description="Двухкомнатный номер", rules="VIP обслуживание"),
        ]
        db.session.add_all(cats)
        db.session.flush()
        rooms = [
            Room(number="101", floor=1, capacity=2, price=4500, category_id=cats[0].id),
            Room(number="102", floor=1, capacity=2, price=4500, category_id=cats[0].id),
            Room(number="201", floor=2, capacity=3, price=6800, category_id=cats[1].id),
            Room(number="301", floor=3, capacity=4, price=11900, category_id=cats[2].id),
        ]
        db.session.add_all(rooms)
        services = [
            Service(name="Завтрак", price=900, unit="сутки", description="Шведский стол"),
            Service(name="Трансфер", price=2500, unit="услуга", description="Трансфер до аэропорта"),
            Service(name="Парковка", price=500, unit="сутки", description="Охраняемая парковка"),
        ]
        db.session.add_all(services)
        db.session.commit()


def ensure_admin(email: str, password: str, full_name: str = "Системный администратор"):
    seed_all()
    admin_role = Role.query.filter_by(name="Администратор").first()
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, full_name=full_name, role=admin_role)
        user.set_password(password)
        db.session.add(user)
    else:
        user.full_name = full_name
        user.role = admin_role
        user.set_password(password)
    db.session.commit()
    return user
