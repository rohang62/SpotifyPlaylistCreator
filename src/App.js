import React from 'react';
import './App.css';
import LoginScreen from './login_screen';

export default class App extends React.Component {
  render() {
    return (
      <div className="App">
        <LoginScreen />
      </div>
    );
  }
}
