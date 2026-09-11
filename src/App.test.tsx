import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi, type MockInstance } from 'vitest';
import App from './App';
import { ErrorBoundary } from './ErrorBoundary';

describe('App shell', () => {
  it('renders the product heading', () => {
    render(<App />);
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('REXCOX');
  });
});

describe('ErrorBoundary', () => {
  let consoleError: MockInstance<typeof console.error>;

  beforeEach(() => {
    // React logs caught render errors; silence them so output stays readable.
    consoleError = vi.spyOn(console, 'error').mockImplementation(() => undefined);
  });

  function Boom(): React.ReactElement {
    throw new Error('boom');
  }

  it('renders children when nothing throws', () => {
    render(
      <ErrorBoundary>
        <p>safe</p>
      </ErrorBoundary>,
    );
    expect(screen.getByText('safe')).toBeInTheDocument();
  });

  it('renders the fallback instead of crashing the tree', () => {
    render(
      <ErrorBoundary>
        <Boom />
      </ErrorBoundary>,
    );
    expect(screen.getByRole('alert')).toBeInTheDocument();
    expect(screen.getByTestId('error-boundary-message')).toHaveTextContent('boom');
    expect(consoleError).toHaveBeenCalled();
  });

  it('prefers an explicit fallback when provided', () => {
    render(
      <ErrorBoundary fallback={<p>custom</p>}>
        <Boom />
      </ErrorBoundary>,
    );
    expect(screen.getByText('custom')).toBeInTheDocument();
  });
});
