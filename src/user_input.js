import React from 'react';
import logo from './spotify_logo.svg';
import './App.css';
import LoginScreen from './login_screen';
import PlaylistDisplay from './playlist_display';

export default class UserInput extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      state: 1,
      username: props.state.username,
      minutes: 100,
      name: '',
    };
    this.updateSlider = this.updateSlider.bind(this);
    this.changeName = this.changeName.bind(this);
    this.handleSubmitLogin = this.handleSubmitLogin.bind(this);
    this.handleSubmitCreate = this.handleSubmitCreate.bind(this);
  }

  changeName(event) {
    this.setState({ name: event.target.value });
  }

  updateSlider(event) {
    this.setState({ minutes: event.target.value });
  }

  handleSubmitLogin() {
    this.setState({ state: 0 });
  }

  handleSubmitCreate() {
    this.setState({ state: 2 });
  }

  render() {
    if (this.state.state === 0) {
      return (
        <div className="App">
          <LoginScreen state={this.state} />
        </div>
      );
    } if (this.state.state === 1) {
      return (
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <div>
              <label>
                Name of Playlist to create:
                <input
                  type="text"
                  value={this.state.name}
                  onChange={this.changeName}
                />
              </label>
            </div>
            <div>
              <label>
                Length of Playlist:
                <input
                  type="range"
                  min="10"
                  max="600"
                  value="100"
                  value={this.state.minutes}
                  onChange={this.updateSlider}
                />
                {this.state.minutes}
                {' '}
                minutes
              </label>
            </div>
            <div>
              <button className="button" onClick={this.handleSubmitLogin}> Go back to Login </button>
              <div className="divider" />
              <button
                className="button"
                onClick={this.handleSubmitCreate}
                disabled={this.state.name === ''}
              >
                {' '}
                Create Playlist
              </button>
            </div>
          </header>
        </div>
      );
    }
    return (
      <div className="App">
        <PlaylistDisplay state={this.state} />
      </div>
    );
  }
}
