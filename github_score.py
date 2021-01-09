# %% Imports
from github import Github
g = Github("037b7a7163ced7b073fa1ac82ad52642ef0c125b")


##################### Comits ###############



def show(user_name):
  user = g.get_user(user_name)
  repo = user.get_repos()[0]
  commits = repo.get_commits()

  # modifiers

  # class modifiers
  m_high=3
  m_med=2
  m_low=1

  # user modifiers
  m_u_public_repos = 2
  m_u_created_at = 3
  m_u_public_gists = 3
  m_u_followers = 1

  # repo modifiers
  m_r_created_at = 1
  m_r_stargazers_count = 2
  m_r_watchers_count = 2
  m_r_forks_count = 3
  m_r_subscribers_count = 2
  m_r_open_issues_count = 1
  m_r_has_projects = 1
  m_r_has_wiki = 1

  # commit modifiers
  m_c_commits = 1

  print("high [3], med [2], low [1]")
  print("")
  print("user class priority:     [{}] HIGH".format(m_high))
  print("user public repos:       [{}] {}".format(m_u_public_repos, user.public_repos))
  print("user created at:         [{}] {}".format(m_u_created_at, user.created_at))
  print("user public gist:        [{}] {}".format(m_u_public_gists, user.public_gists))
  print("user followers:          [{}] {}".format(m_u_followers, user.followers))
  print("")
  print("Single repo example")
  print("")
  print("repo class priority:     [{}] MEDIUM".format(m_med))
  print("repo is forked:          [{}] {}".format("M",repo.fork))
  print("repo created at:         [{}] {}".format(m_r_created_at, repo.created_at))
  print("repo stargazer count:    [{}] {}".format(m_r_stargazers_count,repo.stargazers_count))
  print("repo watchers count:     [{}] {}".format(m_r_watchers_count,repo.watchers_count))
  print("repo fork count:         [{}] {}".format(m_r_forks_count,repo.forks_count))
  print("repo sub count:          [{}] {}".format(m_r_subscribers_count,repo.subscribers_count))
  print("repo open issues:        [{}] {}".format(m_r_open_issues_count,repo.open_issues_count))
  print("repo has projects:       [{}] {}".format("M",repo.has_projects))
  print("repo has wiki:           [{}] {}".format("M",repo.has_wiki))
  print("")
  print("single repo commits example")
  print("")
  print("commit class priority:   [{}] LOW".format(m_low))
  print("commits count:           [{}] {}".format(m_c_commits,commits.totalCount))

  # ================== SCORE ===================

  user_score=0
  repo_score=0
  commit_score=0

  user_score += user.public_repos * m_u_public_repos
  user_score += user.public_gists * m_u_public_gists
  user_score += user.followers * m_u_followers

  # per repo
  current_user_id = user.id
  before_calls = user.raw_headers['x-ratelimit-used']

  print("=================================")
  print("User: ", user.login)
  print("analyzing score, please wait...")

  for repo in user.get_repos():

      if not repo.fork:
          current_repo_score = 0
          current_repo_score += repo.stargazers_count * m_r_stargazers_count
          current_repo_score += repo.watchers_count * m_r_watchers_count
          current_repo_score += repo.forks_count * m_r_forks_count
          current_repo_score += repo.subscribers_count * m_r_subscribers_count
          current_repo_score += repo.open_issues_count * m_r_open_issues_count
          repo_score+=current_repo_score
          commit_score += repo.get_commits().totalCount * m_c_commits

  # apply modifier
  print("applying class modifiers...")
  user_score *= m_high
  repo_score *= m_med
  commit_score *= m_low

  user = g.get_user()
  after_calls = user.raw_headers['x-ratelimit-used']

  print("")
  print("total api calls: ", int(after_calls) - int(before_calls))
  # print("api calls left: ", int(user.raw_headers['x-ratelimit-remaining']))
  
  print("")
  print("user class: ", user_score)
  print("repo class: ", repo_score)
  print("commit class: ", commit_score)
  print("")
  print("total score: ", user_score+repo_score+commit_score)

if __name__ == "__main__":
    show("torvalds")
# %%
