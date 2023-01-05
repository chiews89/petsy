import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import "./auth.css";

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const demoUserLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"));

    if (data) {
      setErrors(data);
    }
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <form onSubmit={onLogin} className="login-form-container">
      <div className="errors-list">
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className="sign_in-container">
        <div className="sign_in-logo">Sign in</div>
        <div>
          <button
            type="button"
            className="demo-user-btn"
            onClick={demoUserLogin}
          >
            Try Demo
          </button>
        </div>
      </div>
      <div id="login-container">
        <div className="login-text-container">
          <label htmlFor="email">Email</label>
        </div>
        <div>
          <input
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            required={true}
            onChange={updateEmail}
            className="email_input-bar"
          />
        </div>
        <div className="login-text-container">
          <label htmlFor="password">Password</label>
        </div>
        <div>
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            required={true}
            onChange={updatePassword}
            className="password_input-bar"
          />
        </div>
          <button type="submit" className="sign_in-btn">
            Sign in
          </button>
          <p className="petsy-policy"> By clicking Sign in, you agree to Petsy's Terms of Use and Privacy
            Policy, which does not exist. Petsy will not send you
            communications and post without your permission.</p>
      </div>
    </form>
  );
};

export default LoginForm;
