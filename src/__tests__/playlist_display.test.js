import React from "react";
import renderer from "react-test-renderer";
import PlaylistDisplay from "./../playlist_display";
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';

/*jest.mock('axios', () => ({
    __esModule: true,
    post: jest.fn(() => Promise.resolve('test')),
    default: jest.fn(() => Promise.resolve('test')),
}));*/

test("renders loading screen", () => {
	let state = { name : '', username : '', minutes : 0 };
	const Tree = renderer.create(<PlaylistDisplay state = {state}/>).toJSON();
	expect(Tree).toMatchSnapshot();
});

function timeout(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

test("renders success screen", async () => {
	var mock = new MockAdapter(axios);
	let state = { name : '', username : '', minutes : 0 };
	mock.onPost('http://localhost:8000/create').reply(200, "test success");
	const asFragment = renderer.create(<PlaylistDisplay state = {state}/>);
	await timeout(3000);
	const tree = asFragment.toJSON();
	expect(tree).toMatchSnapshot();
});

test("renders error screen", async () => {
	var mock = new MockAdapter(axios);
	let state = { name : '', username : '', minutes : 0 };
	mock.onPost('http://localhost:8000/create').reply(400, "test error");
	const asFragment = renderer.create(<PlaylistDisplay state = {state}/>);
	await timeout(3000);
	const tree = asFragment.toJSON();
	expect(tree).toMatchSnapshot();
});
