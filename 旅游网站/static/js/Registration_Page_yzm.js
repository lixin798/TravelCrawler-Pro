function generateCaptcha() {
    const characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    let captcha = '';
    for (let i = 0; i < 4; i++) {
        captcha += characters.charAt(Math.floor(Math.random() * characters.length));
        console.log("正在生成验证码字符: " + characters.charAt(Math.floor(Math.random() * characters.length)));
    }
    console.log("生成的验证码: " + captcha);
    return captcha;
}

document.getElementById('generateCaptchaButton').addEventListener('click', function () {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;
    if (username === '') {
        alert('请填写账号');
        return;
    }
    if (!validatePassword(password)) {
        return;
    }
    if (!validateEmail(email)) {
        return;
    }
    const newCaptcha = generateCaptcha();
    document.getElementById('captchaText').textContent = newCaptcha;
});

// 获取验证码相关元素和注册按钮
const captchaInput = document.getElementById('captcha');
const captchaTextElement = document.getElementById('captchaText');
const registerButton = document.querySelector('form input[type="submit"]');

// 密码长度验证
function validatePassword(password) {
    if (password.length < 8) {
        alert('密码少于8位数');
        return false;
    } else if (password.length >= 14) {
        alert('密码长度不能超过14位');
        return false;
    }
    return true;
}

// 邮箱格式验证
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!re.test(String(email).toLowerCase())) {
        alert('Email格式错误');
        return false;
    }
    return true;
}

// 确认密码验证
function validateConfirmPassword(password, confirmPassword) {
    if (password !== confirmPassword) {
        alert('两次输入的密码不一致');
        return false;
    }
    return true;
}

// 账号验证提示
const usernameInput = document.getElementById('username');
usernameInput.addEventListener('blur', function () {
    if (usernameInput.value === '') {
        alert('请填写账号');
    }
});

// 为注册按钮添加点击事件监听器
registerButton.addEventListener('click', function (e) {
    e.preventDefault(); // 阻止表单默认提交行为
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const captchaValue = captchaInput.value;
    const generatedCaptcha = captchaTextElement.textContent;

    if (username === '') {
        alert('请填写账号');
        return;
    }
    if (!validatePassword(password)) {
        return;
    }
    if (!validateConfirmPassword(password, confirmPassword)) {
        return;
    }
    if (!validateEmail(email)) {
        return;
    }
    if (captchaValue === generatedCaptcha) {
        // 将用户名和密码存储到localStorage
        localStorage.setItem('registeredUsername', username);
        localStorage.setItem('registeredPassword', password);
        // 跳转到主页
        window.location.href = 'http://127.0.0.1:8848/%E4%B8%BB%E9%A1%B5/index.html';
    } else {
        alert('验证码输入错误，请重新输入验证码');
    }
});