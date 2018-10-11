from info import create_app, db
from flask_script import Manager


from flask_migrate import MigrateCommand, Migrate

app = create_app('development')

manager = Manager(app)
# 为数据库迁移做准备
Migrate(app, db)
manager.add_command('db', MigrateCommand)





if __name__ == '__main__':
    manager.run()
