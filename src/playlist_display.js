import React from 'react';
import axios from 'axios';
import logo from './spotify_logo.svg';
import './App.css';
import LoginScreen from './login_screen';

const BASE_URL = 'http://localhost:8000/';

export default class PlaylistDisplay extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			state: 1,
			username: props.state.username,
			minutes: props.state.minutes,
			name: props.state.name,
			res: {},
			error: '',
		};
		this.handleSubmitLogin = this.handleSubmitLogin.bind(this);
	}

	componentDidMount() {
		const url = `${BASE_URL}playlist/create_recommended`;
		const data = {};
		data.user = this.state.username;
		data.name = this.state.name;
		data["length"] = this.state.minutes;
		axios.post(url, data, {
			headers:
			{
				'Access-Control-Allow-Origin': '*',
				'Content-Type': 'application/json',
			},
		})
			.then((res) => {
				this.setState({ res: res.data, state: 2 });
			}).catch((error) => {
				this.setState({
					res: error.text,
					state: 3,
				});
			});
	}

	handleSubmitLogin() {
		this.setState({ state: 0 });
	}

	renderTable() {
		if (this.state.res !== undefined) {
			return this.state.res.map((song, _) => {
				const name = song.name;
				let artist = "";
				let i = 0;
				for (i = 0; i < song.artists.length; i++) {
					artist += song.artists[i].name;
					artist += ", ";
				}
				artist = artist.substring(0, artist.length - 2);
				const image_url = song.album.images[0].url;
				return (
					<tr key={name}>
						<td>
							<img src={image_url} alt='' width='50' height='60'>
							</img>
						</td>
						<td>{name}</td>
						<td>{artist}</td>
					</tr>
				)
			})
		}
	}

	renderTableHeader() {
		let header = ["", "Track Name", "Artists"]
		return header.map((key, index) => {
			return <th key={index}>{key.toUpperCase()}</th>
		})
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
            Loading...
          </header>
				</div>
			);
		} if (this.state.state === 2) {
			return (
				<div className="App">
					<header className="App-header">
						<img src={logo} className="App-logo" alt="logo" />
						<table id='songs'>
							<tbody>
								<tr>{this.renderTableHeader()}</tr>
								{this.renderTable()}
							</tbody>
						</table>
						<button className="button" onClick={this.handleSubmitLogin}> Go back to Login </button>
					</header>
				</div>
			);
		}
		return (
			<div className="App">
				<header className="App-header">
					<img src={logo} className="App-logo" alt="logo" />
					<div className="Incorrect">
						{this.state.error}
					</div>
					<button className="button" onClick={this.handleSubmitLogin}> Go back to Login </button>
				</header>
			</div>
		);
	}
}
