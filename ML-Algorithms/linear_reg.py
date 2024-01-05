import os

def main():
  bn=os.getenv('BUILD_NUMBER', 'Unknown')
  print(f'This is a python build. The Build NUmber is:{bn}')

if __name__=='__main__':
  main()
