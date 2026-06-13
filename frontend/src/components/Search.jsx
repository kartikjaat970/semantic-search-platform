import { useState } from "react";

import api from "../api";

import Result from "./Result";


export default function Search() {
	const [query, setQuery] = useState("");
	const [query, setQuery] = useState("");
	const [answer, setAnswer] = useState("");

	const ask = async () => {
		try {
			const res = await api.post("/chat", { query });
			setAnswer(res.data.answer);
		} catch {
			setAnswer("Backend not ready");
		}
	};

	return (
		<div className="card">
			<h2>Ask AI</h2>

			<input value={query} onChange={e => setQuery(e.target.value)} />

			<button onClick={ask}>Ask</button>

			<Result text={answer} />
		</div>
	);
}