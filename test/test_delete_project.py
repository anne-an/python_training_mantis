import random


def test_delete_project(app, db):
    old_projects = db.get_project_list()
    if not old_projects:
        app.project.create(app.project.generate_random_name())
        old_projects = db.get_project_list()
    rand_project = random.choice(old_projects)
    app.project.delete(rand_project)
    new_projects = db.get_project_list()
    old_projects.remove(rand_project)
    assert old_projects == new_projects
