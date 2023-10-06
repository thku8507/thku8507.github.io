# Generating path to project directory
project_dir = os.path.join(
    pathlib.Path.home(), 'earth-analytics', 'data', 'marshall-fire')

# Create project directory
os.makedirs(project_dir, exist_ok=True)

project_dir