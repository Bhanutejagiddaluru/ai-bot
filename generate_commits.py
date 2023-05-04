import os
import random
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2023, 1, 1)  # Start date for contributions within the last year
end_date = datetime(2023, 12, 31)  # End date for contributions
repo_path = "."  # Path to your GitHub repository, '.' means current directory
user_email = "giddalurubhanuteja@gmail.com"  # Your GitHub email

# Generate random dates within the specified period
date_range = end_date - start_date
commit_dates = [start_date + timedelta(days=random.randint(0, date_range.days)) for _ in range(50)]  # Adjust the number of commits

# Create commits
for commit_date in commit_dates:
    date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    with open(os.path.join(repo_path, 'commit_file.txt'), 'a') as file:
        file.write(f'Commit on {date_str}\n')
    os.system(f'cd {repo_path} && git add commit_file.txt')
    os.system(f'cd {repo_path} && git -c user.email="{user_email}" commit --date="{date_str}" -m "Commit on {date_str}"')

# Push changes
os.system(f'cd {repo_path} && git push origin main')

print("Commits generated and pushed successfully!")
