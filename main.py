import yaml

def load_tasks():
    with open('builds/tasks.yaml', 'r') as file:
        tasks_data = yaml.safe_load(file)
    return tasks_data

def load_builds():
    with open('builds/builds.yaml', 'r') as file:
        builds_data = yaml.safe_load(file)
    return builds_data

def get_dependent_tasks(task_name, tasks_data):
    dependent_tasks = []
    for task in tasks_data['tasks']:
        print(task)
        if task['name'] == task_name:
            dependencies = task.get('dependencies', [])
            for dependency in dependencies:
                dependent_tasks.append(dependency)
    return dependent_tasks

def get_sorted_tasks(build_name, builds_data, tasks_data):
    build_tasks = None
    for build in builds_data['builds']:
        if build['name'] == build_name:
            build_tasks = build.get('tasks', [])
            break

    if build_tasks is None:
        return []

    sorted_tasks = []
    visited = set()
    temp_visited = set()

    def dfs(task):
        if task in temp_visited:
            raise Exception("Cyclic dependency detected!")
        if task not in visited:
            temp_visited.add(task)
            dependencies = get_dependent_tasks(task, tasks_data)
            for dependency in dependencies:
                dfs(dependency)
            temp_visited.remove(task)
            visited.add(task)
            sorted_tasks.append(task)

    try:
        for task in build_tasks:
            dfs(task)
    except Exception as e:
        print(e)
        return []

    sorted_tasks.reverse()
    return sorted_tasks


if __name__ == '__main__':
    tasks_data = load_tasks()
    builds_data = load_builds()
    build_name = "forward_interest"  # Имя сборки, которую вы хотите получить
    sorted_tasks = get_sorted_tasks(build_name, builds_data, tasks_data)
    print(sorted_tasks)
