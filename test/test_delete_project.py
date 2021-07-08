import random


def test_delete_project(app, db):
    old_projects = app.soap.get_projects()
    if not old_projects:
        app.project.create(app.project.generate_random_name())
        old_projects = app.soap.get_projects()
    rand_project = random.choice(old_projects)
    app.project.delete(rand_project)
    new_projects = app.soap.get_projects()
    old_projects.remove(rand_project)
    assert old_projects == new_projects
