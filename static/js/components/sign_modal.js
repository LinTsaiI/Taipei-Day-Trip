class Modal extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = `
    <div class='modal_background'>
      <div class='modal' id='signin_form'>
        <div class='form_top'></div>
        <div class='modal_content'>
          <img class='close_icon' src='../static/img/icon_close.png' id='close_signin'>
          <form class='sign_form'>
            <div class='form_title'>登入會員帳號</div>
            <input type='text' class='input' name='email' placeholder='輸入電子信箱' id='signin_email'>
            <input type='password' class='input' name='password' placeholder='輸入密碼' id='signin_password'><br>
            <input type='button' value='登入帳戶' class='submit_btn' id='signin_btn'>
            <div class='message' id='signin_msg'></div>
            <div class='switch' id='switch_signup'>還沒有帳戶？點此註冊</div>
          </form>
        </div>
      </div>
      <div class='modal' id='signup_form'>
        <div class='form_top'></div>
        <div class='modal_content'>
          <img class='close_icon' src='../static/img/icon_close.png' id='close_signup'>
          <form class='sign_form'>
            <div class='form_title'>註冊會員帳號</div>
            <input type='text' class='input' name='name' placeholder='輸入姓名' id='signup_name'>
            <input type='text' class='input' name='email' placeholder='輸入電子信箱' id='signup_email'>
            <input type='password' class='input' name='password' placeholder='輸入密碼' id='signup_password'><br>
            <input type='button' value='註冊新帳戶' class='submit_btn' id='signup_btn'>
            <div class='message' id='signup_msg'></div>
            <div class='switch' id='switch_signin'>已經有帳戶了？點此登入</div>
          </form>
        </div>
      </div>
    </div>
    `;
  }
}

customElements.define('modal-component', Modal);