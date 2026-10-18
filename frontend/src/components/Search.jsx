import { useState } from "react";

import api from "../api";

import Result from "./Result";


export default function Search() {
	const [query, setQuery] = useState("");
	const [results, setResults] = useState(null); // null = nothing searched yet
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState("");

	const search = async (e) => {
		e.preventDefault();
		if (!query.trim()) return;

		setLoading(true);
		setError("");
		try {
			const res = await api.post("/search", { text: query });
			setResults(res.data);
		} catch {
			setResults(null);
			setError("Search failed. Is the backend running?");
		} finally {
			setLoading(false);
		}
	};

	return (
		<div className="card">
			<h2>Search</h2>

			<form onSubmit={search}>
				<input
					value={query}
					onChange={e => setQuery(e.target.value)}
					placeholder="Ask in natural language..."
				/>
				<button type="submit" disabled={loading || !query.trim()}>
					{loading ? "Searching..." : "Search"}
				</button>
			</form>

			{error && <p className="error">{error}</p>}

			<Result results={results} />
		</div>
	);
}
