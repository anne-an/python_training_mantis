def test_add_project(app, db):
    old_projects = app.soap.get_projects()
    rand_name = app.project.generate_random_name()
    while rand_name in old_projects:
        rand_name = app.project.generate_random_name()
    app.project.create(rand_name)
    new_projects = app.soap.get_projects()
    old_projects.append(rand_name)
    assert sorted(old_projects) == sorted(new_projects)
