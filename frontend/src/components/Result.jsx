export default function Result({ results }) {
	if (results === null) return null;

	if (results.length === 0) {
		return <p>No results. Upload some text first.</p>;
	}

	return (
		<div>
			<h3>Results</h3>
			{results.map((r, i) => (
				<div className="result" key={i}>
					<span className="score">{Math.round(r.score * 100)}% match</span>
					<p>{r.text}</p>
				</div>
			))}
		</div>
	);
}
