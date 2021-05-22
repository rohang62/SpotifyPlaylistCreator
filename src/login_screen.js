import React from 'react';
import logo from './spotify_logo.svg';
import './App.css';
import { username, password } from './login_details';
import IncorrectLogin from './incorrect_login';
import UserInput from './user_input';

export default class LoginScreen extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      logged: 0,
    };
    this.changeUsername = this.changeUsername.bind(this);
    this.changePassword = this.changePassword.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  changeUsername(event) {
    this.setState({ username: event.target.value });
  }

  changePassword(event) {
    this.setState({ password: event.target.value });
  }

  handleSubmit() {
    if (username === this.state.username && password === this.state.password) {
      this.setState({ logged: 2 });
      window.open(
        'http://localhost:8000/authenticate', '_blank',
      );
    } else {
      this.setState({ logged: 1 });
    }
  }

  render() {
    if (this.state.logged === 0) {
      return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <div>
              <label>
                Username:
                <input
                  type="text"
                  value={this.state.username}
                  onChange={this.changeUsername}
                />
              </label>
            </div>
            <div>
              <label>
                Password:
                <input
                  type="password"
                  value={this.state.password}
                  onChange={this.changePassword}
                />
              </label>
            </div>
            <br />
            <button className="button" onClick={this.handleSubmit}> Submit </button>
          </header>
        </div>
      );
    } if (this.state.logged === 1) {
      return (
        <div className="App">
          <IncorrectLogin state={this.state} />
        </div>
      );
    }
    return (
      <div className="App">
        <UserInput state={this.state} />
      </div>
    );
  }
}
