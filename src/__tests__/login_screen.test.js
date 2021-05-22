import React from "react";
import renderer from "react-test-renderer";
import LoginScreen from "./../login_screen";

test("renders login screen", () => {
	const Tree = renderer.create(<LoginScreen />).toJSON();
	expect(Tree).toMatchSnapshot();
});
