import os

REPOSITORIES = {
  'weko2.rdm.nii.ac.jp': {
     'host': 'https://weko2.rdm.nii.ac.jp/weko/sword/', 
     'client_id': os.environ['WEKO_CLIENT_ID'], 
     'client_secret': os.environ['WEKO_CLIENT_SECRET'], 
     'authorize_url': 'https://weko2.rdm.nii.ac.jp/oauth/authorize.php', 
     'access_token_url': 'https://weko2.rdm.nii.ac.jp/oauth/token.php'
  }
}
REPOSITORY_IDS = list(sorted(REPOSITORIES.keys()))
