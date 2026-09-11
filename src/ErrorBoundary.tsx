import { Component, type ErrorInfo, type ReactNode } from 'react';

interface ErrorBoundaryProps {
  children: ReactNode;
  fallback?: ReactNode;
}

interface ErrorBoundaryState {
  error: Error | null;
}

/**
 * Catches render/lifecycle errors anywhere below it so a single bad component
 * cannot blank out the whole application.
 */
export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  override state: ErrorBoundaryState = { error: null };

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { error };
  }

  override componentDidCatch(error: Error, info: ErrorInfo): void {
    console.error('Unhandled UI error:', error, info.componentStack);
  }

  override render(): ReactNode {
    const { error } = this.state;

    if (error) {
      return (
        this.props.fallback ?? (
          <div role="alert" className="error-boundary">
            <h1>Something went wrong</h1>
            <p data-testid="error-boundary-message">{error.message}</p>
          </div>
        )
      );
    }

    return this.props.children;
  }
}
