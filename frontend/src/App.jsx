import "./index.css";

import Upload from "./components/Upload";
import Search from "./components/Search";

function App() {
	return (
		<div className="container">
			<h1>AI Semantic Search</h1>

			<Upload />

			<Search />
		</div>
	);
}

export default App;