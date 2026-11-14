import { useState } from "react";
import "./index.css";

import Upload from "./components/Upload";
import Search from "./components/Search";

function App() {
	// The upload pop-up opens first; closing it leads to the search page
	const [showUpload, setShowUpload] = useState(true);

	return (
		<div className="app">
			<header className="topbar">
				<h1>AI Semantic Search</h1>
				<button className="ghost" onClick={() => setShowUpload(true)}>
					Upload documents
				</button>
			</header>

			<main className="container">
				<Search />
			</main>

			{showUpload && <Upload onClose={() => setShowUpload(false)} />}
		</div>
	);
}

export default App;
