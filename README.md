![Platform](https://img.shields.io/badge/platform-MacOS%20%7C%20Windows-6d9fba) [![Release](https://img.shields.io/badge/Release-V1.0-fc1ba6)](https://github.com/yoons100/Resolume-ClearKey/releases) [![License](https://img.shields.io/github/license/yoons100/Resolume-ClearKey)](https://github.com/yoons100/Resolume-ClearKey/blob/main/LICENSE)

## Resolume Clear Hotkey V1.0

ResolumeClearHotkey is a simple system tray App that assigns the **Ctrl + Delete** shortcut to clear selected clips in Resolume.  
  

<img width="192" height="67" alt="h1" src="https://github.com/user-attachments/assets/ad12eb51-c3a5-4f00-a3eb-c334d80768d4" />  
  

<img width="184" height="54" alt="h2" src="https://github.com/user-attachments/assets/755d04ed-9982-4532-b541-7a5ae2e6e904" />  
  
<img width="150" height="70" alt="arenadel01" src="https://github.com/user-attachments/assets/9d48530b-3be0-44fe-9645-f61e7b20149a" />


### How to Use

1. Launch the App.
   - A gray DEL icon will appear in the Windows system tray.

2. Start Resolume.
   - The tray icon will turn green when the App successfully connects to the Resolume API.

3. Select one or more clips in Resolume.

4. Press **Ctrl + Delete**.
   - The selected clips will be cleared automatically.

### Notes

#### 1. Resolume API Configuration Required

This App uses the Resolume REST API.

In Resolume, open:

**Preferences → Webserver**

Enable the Webserver and configure:

- Listen Port: **8880 ~ 8889**
- Listen Address: **127.0.0.1**

<img width="462" height="352" alt="h3" src="https://github.com/user-attachments/assets/79de3a0b-515a-43c2-b706-25bbfc2455cc" />


#### 2. Sequential Deletion

Selected clips are cleared one by one through the API.

For this reason, **Undo (Ctrl + Z)** is also applied sequentially and must be pressed multiple times to restore multiple deleted clips.

#### 3. Security Notice

**[Windows]**
When launching the application for the first time, Windows may display a security warning because the application is not digitally signed.

**[macOS]**
When launching the App for the first time, the **Privacy & Security** window may appear.

Enable the App as an **Input Monitoring** app, then restart the App.

#### 4. Notes

This is a lightweight utility that activates the hotkey only when Resolume is running.

For convenient operation, it is recommended to register the App to start automatically when the computer boots and keep the tray/menu bar icon visible.

**[Windows]**
- Add the App to **Startup**
- Enable the tray icon from:
  **Taskbar Settings → Other System Tray Icons**

**[macOS]**
- Move the App to the **Applications** folder
- Register it from:
  **System Settings → General → Login Items**

---

#### Tray Icon Status

- Gray icon: Not connected
- Green icon: Connected to Resolume API

---

## Resolume ClearHotkey V1.0

ResolumeClearHotkey는 Resolume에서 클립 삭제(Clear)를 **Ctrl + Delete** 단축키로 실행할 수 있도록 해주는 간단한 시스템 트레이 앱입니다.
  

<img width="192" height="67" alt="h1" src="https://github.com/user-attachments/assets/ad12eb51-c3a5-4f00-a3eb-c334d80768d4" />  
  

<img width="184" height="54" alt="h2" src="https://github.com/user-attachments/assets/755d04ed-9982-4532-b541-7a5ae2e6e904" />  
  
<img width="150" height="70" alt="arenadel01" src="https://github.com/user-attachments/assets/9d48530b-3be0-44fe-9645-f61e7b20149a" />

### 사용방법

1. 앱을 실행합니다.
   - Windows 시스템 트레이에 회색 DEL 아이콘이 표시됩니다.

2. Resolume을 실행합니다.
   - Resolume API와 연결되면 트레이 아이콘이 녹색으로 변경됩니다.

3. 삭제할 클립을 1개 또는 여러 개 선택합니다.

4. **Ctrl + Delete** 단축키를 누릅니다.
   - 선택된 클립이 자동으로 삭제됩니다.

### 참고사항

#### 1. Resolume API 설정 필요

이 앱은 Resolume REST API를 사용합니다.

Resolume에서 다음 메뉴를 열어 설정해 주세요.

**설정(Preferences) → Webserver**

다음과 같이 설정합니다.

- Listen Port : **8880 ~ 8889**
- Listen Address : **127.0.0.1**

<img width="462" height="352" alt="h3" src="https://github.com/user-attachments/assets/79de3a0b-515a-43c2-b706-25bbfc2455cc" />

#### 2. 순차 삭제 방식

선택된 클립은 API를 통해 하나씩 순차적으로 삭제됩니다.

따라서 **되돌리기(Ctrl + Z)** 역시 순차적으로 적용되며, 여러 개의 클립을 복구하려면 Ctrl + Z를 여러 번 눌러야 합니다.

#### 3. 보안 안내

**[Windows]**
앱을 처음 실행할 때, 인증된 디지털 서명이 없는 앱이라는 보안 경고가 표시될 수 있습니다.

**[macOS]**
앱을 처음 실행할 때 **개인정보 보호 및 보안(Privacy & Security)** 창이 표시될 수 있습니다.

앱을 **입력 모니터링(Input Monitoring)** 앱으로 활성화한 후 앱을 다시 실행해 주세요.

#### 4. 참고

이 앱은 Resolume이 실행되어 있을 때만 단축키가 활성화되는 가벼운 유틸리티입니다.

부팅 시 자동 실행되도록 등록하고 시스템 트레이(메뉴바)에 항상 표시되도록 설정하면 더욱 편리하게 사용할 수 있습니다.

**[Windows]**
- 앱을 **시작프로그램(Startup)** 에 등록
- **작업 표시줄 설정 → 기타 시스템 트레이 아이콘** 에서 아이콘 표시 활성화

**[macOS]**
- 앱을 **Applications** 폴더로 이동
- **시스템 설정 → 일반 → 로그인 항목(Login Items)** 에 등록

---

#### 트레이 아이콘 상태

- 회색 아이콘 : 연결 안됨
- 녹색 아이콘 : Resolume API 연결됨

---
