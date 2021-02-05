// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: orbita_kinematics.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Reachy.Sdk.Kinematics {
  public static partial class OrbitaKinematic
  {
    static readonly string __ServiceName = "reachy.sdk.kinematics.OrbitaKinematic";

    static void __Helper_SerializeMessage(global::Google.Protobuf.IMessage message, grpc::SerializationContext context)
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (message is global::Google.Protobuf.IBufferMessage)
      {
        context.SetPayloadLength(message.CalculateSize());
        global::Google.Protobuf.MessageExtensions.WriteTo(message, context.GetBufferWriter());
        context.Complete();
        return;
      }
      #endif
      context.Complete(global::Google.Protobuf.MessageExtensions.ToByteArray(message));
    }

    static class __Helper_MessageCache<T>
    {
      public static readonly bool IsBufferMessage = global::System.Reflection.IntrospectionExtensions.GetTypeInfo(typeof(global::Google.Protobuf.IBufferMessage)).IsAssignableFrom(typeof(T));
    }

    static T __Helper_DeserializeMessage<T>(grpc::DeserializationContext context, global::Google.Protobuf.MessageParser<T> parser) where T : global::Google.Protobuf.IMessage<T>
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (__Helper_MessageCache<T>.IsBufferMessage)
      {
        return parser.ParseFrom(context.PayloadAsReadOnlySequence());
      }
      #endif
      return parser.ParseFrom(context.PayloadAsNewBuffer());
    }

    static readonly grpc::Marshaller<global::Reachy.Sdk.Kinematics.OrbitaTarget> __Marshaller_reachy_sdk_kinematics_OrbitaTarget = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.Sdk.Kinematics.OrbitaTarget.Parser));
    static readonly grpc::Marshaller<global::Reachy.Sdk.Kinematics.JointsPosition> __Marshaller_reachy_sdk_kinematics_JointsPosition = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.Sdk.Kinematics.JointsPosition.Parser));

    static readonly grpc::Method<global::Reachy.Sdk.Kinematics.OrbitaTarget, global::Reachy.Sdk.Kinematics.JointsPosition> __Method_ComputeOrbitaIK = new grpc::Method<global::Reachy.Sdk.Kinematics.OrbitaTarget, global::Reachy.Sdk.Kinematics.JointsPosition>(
        grpc::MethodType.Unary,
        __ServiceName,
        "ComputeOrbitaIK",
        __Marshaller_reachy_sdk_kinematics_OrbitaTarget,
        __Marshaller_reachy_sdk_kinematics_JointsPosition);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Reachy.Sdk.Kinematics.OrbitaKinematicsReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of OrbitaKinematic</summary>
    [grpc::BindServiceMethod(typeof(OrbitaKinematic), "BindService")]
    public abstract partial class OrbitaKinematicBase
    {
      public virtual global::System.Threading.Tasks.Task<global::Reachy.Sdk.Kinematics.JointsPosition> ComputeOrbitaIK(global::Reachy.Sdk.Kinematics.OrbitaTarget request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for OrbitaKinematic</summary>
    public partial class OrbitaKinematicClient : grpc::ClientBase<OrbitaKinematicClient>
    {
      /// <summary>Creates a new client for OrbitaKinematic</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public OrbitaKinematicClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for OrbitaKinematic that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public OrbitaKinematicClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected OrbitaKinematicClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected OrbitaKinematicClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::Reachy.Sdk.Kinematics.JointsPosition ComputeOrbitaIK(global::Reachy.Sdk.Kinematics.OrbitaTarget request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ComputeOrbitaIK(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Reachy.Sdk.Kinematics.JointsPosition ComputeOrbitaIK(global::Reachy.Sdk.Kinematics.OrbitaTarget request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_ComputeOrbitaIK, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Reachy.Sdk.Kinematics.JointsPosition> ComputeOrbitaIKAsync(global::Reachy.Sdk.Kinematics.OrbitaTarget request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ComputeOrbitaIKAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Reachy.Sdk.Kinematics.JointsPosition> ComputeOrbitaIKAsync(global::Reachy.Sdk.Kinematics.OrbitaTarget request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_ComputeOrbitaIK, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override OrbitaKinematicClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new OrbitaKinematicClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(OrbitaKinematicBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_ComputeOrbitaIK, serviceImpl.ComputeOrbitaIK).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, OrbitaKinematicBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_ComputeOrbitaIK, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Reachy.Sdk.Kinematics.OrbitaTarget, global::Reachy.Sdk.Kinematics.JointsPosition>(serviceImpl.ComputeOrbitaIK));
    }

  }
}
#endregion
