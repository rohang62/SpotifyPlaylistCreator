import React from "react";
import renderer from "react-test-renderer";
import IncorrectLogin from "./../incorrect_login";

test("renders incorrect login screen", () => {
	let state = { username : '', password : '' };
	const Tree = renderer.create(<IncorrectLogin state = {state}/>).toJSON();
	expect(Tree).toMatchSnapshot();
});
