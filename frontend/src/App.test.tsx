import { render, screen } from "@testing-library/react";
import { App } from "./App";

describe("App", () => {
  it("renders application heading", () => {
    render(<App />);
    expect(screen.getByText("DocuGuard Knowledge Hub")).toBeInTheDocument();
  });
});
