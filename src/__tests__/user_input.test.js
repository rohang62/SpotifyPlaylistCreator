import React from "react";
import renderer from "react-test-renderer";
import UserInput from "./../user_input";

test("renders user input screen", () => {
	let state = { username : '', password : '' };
	const Tree = renderer.create(<UserInput state = {state}/>).toJSON();
	expect(Tree).toMatchSnapshot();
});
