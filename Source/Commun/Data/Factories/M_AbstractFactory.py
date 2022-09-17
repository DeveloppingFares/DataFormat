from Source.Commun.Data.Utilitaires.M_Constantes import E_Format


class C_AbstractFactory:
    def __class_getitem__(cls, format_element: E_Format) -> type:
        if format_element == E_Format.package:
            from Source.Commun.Data.Factories.M_PackageFactory import C_PackageFactory
            return C_PackageFactory
        elif format_element == E_Format.bitfield:
            from Source.Commun.Data.Factories.M_BitfieldFactory import C_BitfieldFactory
            return C_BitfieldFactory
        elif format_element == E_Format.buffer:
            from Source.Commun.Data.Factories.M_BufferFactory import C_BufferFactory
            return C_BufferFactory
        elif format_element == E_Format.enumerate:
            from Source.Commun.Data.Factories.M_EnumerateFactory import C_EnumerateFactory
            return C_EnumerateFactory
        elif format_element == E_Format.processed:
            from Source.Commun.Data.Factories.M_ProcessedFactory import C_ProcessedFactory
            return C_ProcessedFactory
        elif format_element == E_Format.range:
            from Source.Commun.Data.Factories.M_RangeFactory import C_RangeFactory
            return C_RangeFactory
        elif format_element == E_Format.field:
            from Source.Commun.Data.Factories.M_FieldFactory import C_FieldFactory
            return C_FieldFactory
        elif format_element == E_Format.reference:
            from Source.Commun.Data.Factories.M_ReferenceFactory import C_ReferenceFactory
            return C_ReferenceFactory
        elif format_element == E_Format.dependance:
            from Source.Commun.Data.Factories.M_DependanceFactory import C_DependanceFactory
            return C_DependanceFactory
        else:
            raise NotImplementedError
