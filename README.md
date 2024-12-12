# HA를 이용한 공장 자동화 Matter 허브

## 초기 설정

1. 먼저 HA core를 가져옵니다.
```
git submodule update --init
```

1. VScode devcontianer를 이용해서 Container를 만듭니다.
```
Dev containers: Rebuild and Reopen containers
```

1. VScode task 기능을 이용해서 Home Assistant를 실행합니다.
```
Tasks: Run Task
```
OnBoarding 과정이 끝난 후에 HA가 동작하지 않으면 Ctrl-F5를 눌러 봅니다.

1. 개발용 custom component를 홈 어시스턴트에 넣습니다. 컨테이너의 콘솔을 열어주십시오.
```
vscode ➜ /workspaces/HA-matter-hub (main) $ cd core/config
vscode ➜ /workspaces/HA-matter-hub/core/config (dev) $ ln -sf ../../custom_components .
vscode ➜ /workspaces/HA-matter-hub/core/config (dev) $
```

1. HA configuration.yaml 을 수정합니다.
```
tia_fake_hub:
```

1. HA 를 다시 시작합니다.


```
vscode ➜ /workspaces/HA-matter-hub (main) $ cd core/config
vscode ➜ /workspaces/HA-matter-hub/core/config (dev) $ ln -sf ../../_config/python_scripts .
vscode ➜ /workspaces/HA-matter-hub/core/config (dev) $ ln -sf ../../_config/automations.yaml .
vscode ➜ /workspaces/HA-matter-hub/core/config (dev) $
```