import { render, screen } from "@testing-library/react";
import type { ReactNode } from "react";
import { App } from "./App";

jest.mock("@chakra-ui/react", () => ({
  Box: ({ children }: { children: ReactNode }) => <div>{children}</div>,
  Heading: ({ children }: { children: ReactNode }) => <h1>{children}</h1>,
  Text: ({ children }: { children: ReactNode }) => <p>{children}</p>,
}));

describe("App", () => {
  it("renders application heading", () => {
    render(<App />);
    expect(screen.getByText("DocuGuard Knowledge Hub")).toBeInTheDocument();
  });
});
