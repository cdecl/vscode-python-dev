## Visual Studio Code, Python 개발환경 구축 

### 1. Visual Studio Code `vscode `
MS가 배포하는 Electron Framwork 기반 Cross-Flatform Code editing

#### 1.1. 설치  
- https://code.visualstudio.com/
- vscode chocolatey 설치 
```
choco install vscode -y 
```

#### ※ Developer Survey Results 2018 : https://insights.stackoverflow.com/survey/2018/

![image](https://user-images.githubusercontent.com/5927142/55314666-905f1c00-54a5-11e9-85b7-d4bb39e6bad4.png)
![image](https://user-images.githubusercontent.com/5927142/55314696-a79e0980-54a5-11e9-853b-e77804fa3305.png)

#### 1.2. 특징 
- Fast, Powerful Editing
	- Linting, multi-cursor editing, parameter hints, and other powerful editing features.
	- Code Navigation and Refactoring
- Meet IntelliSense. 
	- syntax highlighting and autocomplete with IntelliSense, which provides smart completions based on variable types, function definitions, and imported modules.
- Git commands built-in
- Extensible and customizable
	- Install extensions to add new languages, themes, debuggers, and to connect to additional services

#### 1.3. Getting Started, Top Extensions
- https://code.visualstudio.com/docs
- https://marketplace.visualstudio.com/

#### 1.4. 추천 Extensions 
- C/C++ : MS 배포 C/C++ 언어지원   
	- C/C++ IntelliSense, debugging, and code browsing.
	- https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools
- Python : MS 배포 Python 언어지원 
	- Linting, Debugging (multi-threaded, remote), Intellisense, code formatting, refactoring, unit tests, snippets, and more.
	- https://marketplace.visualstudio.com/items?itemName=ms-python.python	
- Code Runner : 코드를 파일 혹은 셀렉션 단위 컴파일(인터프리터) 및 실행 
	- Run C, C++, Java, JS, PHP, Python, Perl, Ruby, Go, Lua, Groovy, PowerShell, CMD, BASH, F#, C#, VBScript, TypeScript, CoffeeScript 등등 
	- Python 언어 이외도 PowerShell, CMD, BASH 등이 지원되어 CLI 환경에서 테스트 대신 편집기에서 바로 실행 가능하게 지원 
	- https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner
- gitignore : gitignore 언어별 선택 및 생성 지원 
	- Language support for .gitignore files. Lets you pull .gitignore files from the https://github.com/github/gitignore repository
	- https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore
- Markdown Preview Github Styling : Github Markdown Style 실시간 보기 
	- Changes VS Code's built-in markdown preview to match Github's style
	- https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles
- Partial Diff : 파일 비교 (Diff) - 클립보드↔파일, 파일↔파일
	- Compare (diff) text selections within a file, across files, or to the clipboard
	- https://marketplace.visualstudio.com/items?itemName=ryu1kn.partial-diff
- REST Client : REST Client 지원, 편집기에 URL 규칙 쓰고 호출 
	- REST Client for Visual Studio Code
	- https://marketplace.visualstudio.com/items?itemName=humao.rest-client
- Gist : github gist 지원 
	- Create, open and edit Gists
	- https://marketplace.visualstudio.com/items?itemName=kenhowardpdx.vscode-gist
- Live Share : MS 배포 실시간 화면 공유 및 편집 (Visual Studio 2019 및 vscode 지원)
	- Real-time collaborative development from the comfort of your favorite tools.
	- https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare


### 2. Python 개발환경 
#### 1.1. 설치 
- Windows : https://www.python.org/
```
choco install python -y 
```

- Linux : `Centos 7`  
```
# 2.7.x 버전은 기본 설치 되어 있음 
# yum 패키지에서 3.4 버전밖에 없어 3.6 설치하려면 epel-release 저장소 추가 
sudo yum install -y epel-release

# python, pip 설치 
sudo yum install python36u python36u-pip

# python3, pip3 사용 하기위한 심볼릭 링크 
sudo ln -sf /usr/bin/python3.6 /usr/bin/python3 
sudo ln -sf /usr/bin/pip3.6 /usr/bin/pip3
```

#### 1.2. PIP 패키지 관리
- Python으로 작성된 패키지 소프트웨어를 설치/관리하는 패키지 관리 시스템

```
# flask 모듈 설치 
# 전역으로 설치하는것으로 linux의 경우 sudo권한이 필요하고 windows 10의 경우 Admin Role 필요 
## 권고 하지 않음 
pip install flask

# flask 모듈을 user 공간에 설치 (권고)
pip install flask --user 

# pip 설치된 모듈 보기 
pip freeze 

# pip 패키지 삭제 
pip uninstall flask
```

#### 1.2.1  virtual 환경  
- 가상환경으로 Python 실행 및 패키지 관리
- virtual 모듈 설치 
	- virtualenv : 일반적으로 많이 사용되는 가상환경 관리 모듈 
```
pip install virtualenv --user 

# linux 의 경우 yum으로도 설치 가능 (3.6 기준)
sudo yum install python36-virtualenv -y 
```

- virtual 만들기 
```
# python 3.6 환경의 virtual 환경 만들기 
virtualenv --python=/usr/bin/python3 venv

# 기본 virtual 환경 만들기
virtualenv venv

# Path 가 없어 명령어를 찾지 못할 경우 
python -m virtualenv venv
```

- activate virtual
```
# linux 
source venv/bin/activate

# windows 
venv\Script\Activate
```

- deactivate virtual
```
# linux 
deactivate

# windows
venv\Scripts\deactivate.bat
```

### 3. Python 개발환경 - vscode 
- Extensions 설치 : Python, Code Runner 
- Python 실행 - Context Menu (mouse right button)
	- Python : Run Python File in Terminal
		- 전체 파일 터미널 실행 
		- virual 환경 지원 : 프로젝트 오픈시 
			- vscode 폴더로 열면 해당 폴더를 기준으로 프로젝트로 인식 
	- Code Runner : Context Menu의 Run Code (Ctrl+Alt+N)
		- 코드 셀렉션 부분 코드 실행 및 전체 파일 실행 
		- virual 환경 지원 안함 

![image](https://user-images.githubusercontent.com/5927142/55136321-7655ce80-5171-11e9-8c3d-6adf59bc0b95.png)

- virtual 환경 선택 : 프로젝트 파일 오픈시 가능 
	- Command palette 열기 (F1 or Ctrl+Shirt+p)
	- Python Select Interpreter → 선택 

![image](https://user-images.githubusercontent.com/5927142/55136987-1cee9f00-5173-11e9-9ebe-f03ba93cd945.png)

![image](https://user-images.githubusercontent.com/5927142/55137002-28da6100-5173-11e9-80c3-fa44e060cd06.png)


