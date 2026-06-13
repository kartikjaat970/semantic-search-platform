export default function Result({ text }) {
  if (!text) return null;

  return (
    <div>
      <h3>Response</h3>
      <p>{text}</p>
    </div>
  );
}